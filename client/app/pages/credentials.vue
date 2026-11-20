<template>
	<form class="space-y-6 max-w-3xl" @submit.prevent="save">
		<div>
			<h2 class="text-xl font-semibold">Réglages</h2>
			<p class="text-sm text-gray-500">
				Clés d'API utilisées pour lister et télécharger tes playlists.
				YouTube ne demande aucune configuration.
			</p>
		</div>

		<SectionCard
			v-for="service in SERVICES"
			:key="service.id"
			:title="service.title"
		>
			<template #actions>
				<a
					:href="service.help"
					target="_blank"
					rel="noopener"
					class="text-sm"
					:class="ACCENTS[service.accent].link"
				>
					Créer une application ↗
				</a>
			</template>

			<div class="grid sm:grid-cols-2 gap-4">
				<label
					v-for="field in service.fields"
					:key="field.key"
					class="block text-sm"
					:class="{ 'sm:col-span-2': 'wide' in field }"
				>
					<span class="block mb-1 font-medium text-gray-700">
						{{ field.label }}
					</span>
					<input
						v-model="form[field.key]"
						type="text"
						autocomplete="off"
						:class="[INPUT_CLASS, ACCENTS[service.accent].ring]"
					>
				</label>
			</div>

			<!-- Connexion du compte Spotify (OAuth) -->
			<div
				v-if="service.id === 'spotify'"
				class="mt-5 pt-5 border-t border-gray-200 space-y-3"
			>
				<div class="flex items-center justify-between gap-4 flex-wrap">
					<p class="text-sm">
						Compte Spotify :
						<span
							class="font-medium"
							:class="spotifyConnected ? 'text-green-700' : 'text-gray-500'"
						>
							{{ spotifyConnected ? "connecté" : "non connecté" }}
						</span>
					</p>
					<div class="flex gap-2">
						<button
							v-if="spotifyConnected"
							type="button"
							:class="SECONDARY_BUTTON_CLASS"
							@click="disconnectSpotify"
						>
							Déconnecter
						</button>
						<button
							type="button"
							:class="[BUTTON_CLASS, ACCENTS.green.button]"
							@click="startSpotifyLogin"
						>
							{{ spotifyConnected ? "Reconnecter" : "Connecter Spotify" }}
						</button>
					</div>
				</div>

				<div v-if="spotifyLoginStarted" class="space-y-2">
					<p class="text-sm text-gray-600">
						Autorise l'accès dans l'onglet Spotify. Tu arrives ensuite sur une
						page qui ne charge pas (<code>{{ spotifyRedirectUri }}</code>), c'est
						normal : copie l'URL complète de la barre d'adresse et colle-la ici.
					</p>
					<div class="flex gap-2">
						<input
							v-model="spotifyRedirectedUrl"
							type="text"
							:placeholder="spotifyRedirectUri + '?code=...'"
							:class="[INPUT_CLASS, ACCENTS.green.ring]"
							@keydown.enter.prevent="finishSpotifyLogin"
						>
						<button
							type="button"
							:disabled="!spotifyRedirectedUrl.trim()"
							:class="[BUTTON_CLASS, ACCENTS.green.button]"
							@click="finishSpotifyLogin"
						>
							Valider
						</button>
					</div>
				</div>

				<p
					v-if="spotifyAuthMessage"
					class="text-sm"
					:class="spotifyAuthOk ? 'text-emerald-600' : 'text-red-600'"
				>
					{{ spotifyAuthMessage }}
				</p>
			</div>
		</SectionCard>

		<div class="flex items-center gap-4">
			<button
				type="submit"
				:disabled="isSaving"
				:class="[BUTTON_CLASS, 'bg-gray-900 hover:bg-gray-700']"
			>
				<LoadingSpinner v-if="isSaving" class="w-4 h-4" />
				Enregistrer
			</button>
			<p
				v-if="saveMessage"
				class="text-sm"
				:class="saveOk ? 'text-emerald-600' : 'text-red-600'"
			>
				{{ saveMessage }}
			</p>
		</div>
	</form>
</template>

<script setup lang="ts">
import { onMounted, ref } from "vue";
import {
	ACCENTS,
	BUTTON_CLASS,
	INPUT_CLASS,
	SECONDARY_BUTTON_CLASS,
} from "~/utils/accents";
import { apiGet, apiPost } from "~/utils/api";

type CredentialKey =
	| "soundcloud_client_id"
	| "soundcloud_client_secret"
	| "soundcloud_user_id"
	| "spotify_client_id"
	| "spotify_client_secret"
	| "spotify_user_id";

const SERVICES = [
	{
		id: "soundcloud",
		title: "SoundCloud",
		accent: "orange",
		help: "https://soundcloud.com/you/apps",
		fields: [
			{ key: "soundcloud_client_id", label: "Client ID" },
			{ key: "soundcloud_client_secret", label: "Client secret" },
			{ key: "soundcloud_user_id", label: "User ID", wide: true },
		],
	},
	{
		id: "spotify",
		title: "Spotify",
		accent: "green",
		help: "https://developer.spotify.com/dashboard",
		fields: [
			{ key: "spotify_client_id", label: "Client ID" },
			{ key: "spotify_client_secret", label: "Client secret" },
			{ key: "spotify_user_id", label: "User ID (optionnel)", wide: true },
		],
	},
] as const satisfies readonly {
	id: string;
	title: string;
	accent: keyof typeof ACCENTS;
	help: string;
	fields: readonly { key: CredentialKey; label: string; wide?: boolean }[];
}[];

const form = ref<Record<CredentialKey, string>>({
	soundcloud_client_id: "",
	soundcloud_client_secret: "",
	soundcloud_user_id: "",
	spotify_client_id: "",
	spotify_client_secret: "",
	spotify_user_id: "",
});

// Enregistrement
const isSaving = ref(false);
const saveMessage = ref("");
const saveOk = ref(true);

async function save() {
	if (!form.value.soundcloud_client_id && !form.value.spotify_client_id) {
		saveOk.value = false;
		saveMessage.value = "Renseigne au moins les clés SoundCloud ou Spotify";
		return;
	}
	isSaving.value = true;
	try {
		await apiPost("/api/credentials/create-or-update", {}, form.value);
		saveOk.value = true;
		saveMessage.value = "Enregistré";
	} catch (err: unknown) {
		saveOk.value = false;
		saveMessage.value =
			err instanceof Error ? err.message : "Erreur lors de l'enregistrement";
	} finally {
		isSaving.value = false;
	}
}

// Connexion du compte Spotify (OAuth)
const spotifyConnected = ref(false);
const spotifyRedirectUri = ref("");
const spotifyLoginStarted = ref(false);
const spotifyRedirectedUrl = ref("");
const spotifyAuthMessage = ref("");
const spotifyAuthOk = ref(true);

async function fetchSpotifyStatus() {
	try {
		const data = await apiGet<{ connected: boolean; redirect_uri: string }>(
			"/api/sp_auth_infos/status",
		);
		spotifyConnected.value = data.connected;
		spotifyRedirectUri.value = data.redirect_uri;
	} catch {
		// backend injoignable : on garde « non connecté »
	}
}

function setAuthMessage(ok: boolean, message: string) {
	spotifyAuthOk.value = ok;
	spotifyAuthMessage.value = message;
}

async function startSpotifyLogin() {
	spotifyAuthMessage.value = "";
	// Ouvert tout de suite (dans le clic) pour ne pas être bloqué comme popup
	const tab = window.open("", "_blank");
	try {
		const data = await apiGet<{ url: string; redirect_uri: string }>(
			"/api/sp_auth_infos/login-url",
		);
		spotifyRedirectUri.value = data.redirect_uri;
		if (tab) tab.location.href = data.url;
		else window.location.href = data.url;
		spotifyLoginStarted.value = true;
	} catch (err: unknown) {
		tab?.close();
		setAuthMessage(false, err instanceof Error ? err.message : "Erreur de connexion Spotify");
	}
}

async function finishSpotifyLogin() {
	try {
		await apiPost("/api/sp_auth_infos/connect", {
			code: spotifyRedirectedUrl.value.trim(),
		});
		setAuthMessage(true, "Compte Spotify connecté");
		spotifyLoginStarted.value = false;
		spotifyRedirectedUrl.value = "";
		await fetchSpotifyStatus();
	} catch (err: unknown) {
		setAuthMessage(false, err instanceof Error ? err.message : "Erreur de connexion Spotify");
	}
}

async function disconnectSpotify() {
	try {
		await apiPost("/api/sp_auth_infos/disconnect");
		setAuthMessage(true, "Compte Spotify déconnecté");
	} catch (err: unknown) {
		setAuthMessage(false, err instanceof Error ? err.message : "Erreur");
	}
	await fetchSpotifyStatus();
}

onMounted(async () => {
	fetchSpotifyStatus();
	try {
		const data = await apiGet<Partial<Record<CredentialKey, string | number | null>> | null>(
			"/api/credentials/",
		);
		if (data) {
			for (const key of Object.keys(form.value) as CredentialKey[]) {
				form.value[key] = data[key]?.toString() ?? "";
			}
		}
	} catch {
		// pas encore de credentials enregistrés
	}
});
</script>
