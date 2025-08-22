<template>
	<div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
		<!-- Header -->
		<header class="bg-white shadow-sm border-b border-gray-200">
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
				<div class="flex justify-between items-center py-6">
					<div class="flex items-center">
						<NuxtLink to="/" class="flex items-center">
							<div
								class="w-10 h-10 bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg flex items-center justify-center"
							>
								<svg
									class="w-6 h-6 text-white"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"
									/>
								</svg>
							</div>
							<h1 class="ml-3 text-2xl font-bold text-gray-900">MinMajDL</h1>
						</NuxtLink>
					</div>
					<div class="flex space-x-4">
						<NuxtLink
							to="/"
							class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors"
						>
							Accueil
						</NuxtLink>
					</div>
				</div>
			</div>
		</header>

		<!-- Main Content -->
		<main class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
			<!-- Page Title -->
			<div class="text-center mb-12">
				<h2 class="text-3xl font-bold text-gray-900 mb-4">
					Configuration des Credentials
				</h2>
				<p class="text-lg text-gray-600">
					Configurez vos clés API pour SoundCloud et Spotify
				</p>
			</div>

			<!-- Credentials Form -->
			<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-8">
				<form class="space-y-8" @submit.prevent="handleSubmit">
					<!-- SoundCloud Section -->
					<div>
						<h3
							class="text-xl font-semibold text-gray-900 mb-6 flex items-center"
						>
							<div
								class="w-8 h-8 bg-orange-100 rounded-lg flex items-center justify-center mr-3"
							>
								<svg
									class="w-5 h-5 text-orange-600"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"
									/>
								</svg>
							</div>
							SoundCloud
						</h3>
						<div class="grid md:grid-cols-2 gap-6">
							<div>
								<label
									for="soundcloud_client_id"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Client ID
								</label>
								<input
									id="soundcloud_client_id"
									v-model="formData.soundcloud_client_id"
									type="text"
									class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
									placeholder="Votre Client ID SoundCloud"
								/>
							</div>
							<div>
								<label
									for="soundcloud_client_secret"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Client Secret
								</label>
								<input
									id="soundcloud_client_secret"
									v-model="formData.soundcloud_client_secret"
									type="text"
									class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
									placeholder="Votre Client Secret SoundCloud"
								/>
							</div>
						</div>
						<div class="mt-4">
							<label
								for="soundcloud_user_id"
								class="block text-sm font-medium text-gray-700 mb-2"
							>
								User ID (optionnel)
							</label>
							<input
								id="soundcloud_user_id"
								v-model="formData.soundcloud_user_id"
								type="text"
								class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
								placeholder="Votre User ID SoundCloud"
							/>
						</div>
					</div>

					<!-- Spotify Section -->
					<div>
						<h3
							class="text-xl font-semibold text-gray-900 mb-6 flex items-center"
						>
							<div
								class="w-8 h-8 bg-green-100 rounded-lg flex items-center justify-center mr-3"
							>
								<svg
									class="w-5 h-5 text-green-600"
									fill="none"
									stroke="currentColor"
									viewBox="0 0 24 24"
								>
									<path
										stroke-linecap="round"
										stroke-linejoin="round"
										stroke-width="2"
										d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"
									/>
								</svg>
							</div>
							Spotify
						</h3>
						<div class="grid md:grid-cols-2 gap-6">
							<div>
								<label
									for="spotify_client_id"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Client ID
								</label>
								<input
									id="spotify_client_id"
									v-model="formData.spotify_client_id"
									type="text"
									class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
									placeholder="Votre Client ID Spotify"
								/>
							</div>
							<div>
								<label
									for="spotify_client_secret"
									class="block text-sm font-medium text-gray-700 mb-2"
								>
									Client Secret
								</label>
								<input
									id="spotify_client_secret"
									v-model="formData.spotify_client_secret"
									type="text"
									class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
									placeholder="Votre Client Secret Spotify"
								/>
							</div>
						</div>
					</div>

					<!-- Submit Button -->
					<div class="flex justify-center pt-6">
						<button
							type="submit"
							:disabled="isLoading"
							class="px-8 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors shadow-lg flex items-center"
						>
							<svg
								v-if="isLoading"
								class="animate-spin -ml-1 mr-3 h-5 w-5 text-white"
								xmlns="http://www.w3.org/2000/svg"
								fill="none"
								viewBox="0 0 24 24"
							>
								<circle
									class="opacity-25"
									cx="12"
									cy="12"
									r="10"
									stroke="currentColor"
									stroke-width="4"
								/>
								<path
									class="opacity-75"
									fill="currentColor"
									d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
								/>
							</svg>
							{{ isLoading ? "Sauvegarde..." : "Sauvegarder les credentials" }}
						</button>
					</div>
				</form>
				<div class="flex justify-center mt-6">
					<NuxtLink
						to="/playlists"
						class="flex items-center justify-center px-8 py-3 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-colors"
					>
						Voir mes playlists
					</NuxtLink>
				</div>

				<!-- Success/Error Messages -->
				<div
					v-if="message"
					class="mt-6 p-4 rounded-lg"
					:class="
						messageType === 'success'
							? 'bg-green-50 text-green-800 border border-green-200'
							: 'bg-red-50 text-red-800 border border-red-200'
					"
				>
					<div class="flex items-center">
						<svg
							v-if="messageType === 'success'"
							class="w-5 h-5 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M5 13l4 4L19 7"
							/>
						</svg>
						<svg
							v-else
							class="w-5 h-5 mr-2"
							fill="none"
							stroke="currentColor"
							viewBox="0 0 24 24"
						>
							<path
								stroke-linecap="round"
								stroke-linejoin="round"
								stroke-width="2"
								d="M6 18L18 6M6 6l12 12"
							/>
						</svg>
						{{ message }}
					</div>
				</div>
			</div>

			<!-- Help Section -->
			<div class="mt-8 bg-blue-50 rounded-xl p-6 border border-blue-200">
				<h4 class="text-lg font-semibold text-blue-900 mb-4 flex items-center">
					<svg
						class="w-5 h-5 mr-2"
						fill="none"
						stroke="currentColor"
						viewBox="0 0 24 24"
					>
						<path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
						/>
					</svg>
					Comment obtenir vos credentials ?
				</h4>
				<div class="space-y-3 text-sm text-blue-800">
					<p>
						<strong>SoundCloud :</strong> Créez une application sur
						<a
							href="https://soundcloud.com/you/apps"
							target="_blank"
							class="underline hover:text-blue-900"
							>soundcloud.com/you/apps</a
						>
					</p>
					<p>
						<strong>Spotify :</strong> Créez une application sur
						<a
							href="https://developer.spotify.com/dashboard"
							target="_blank"
							class="underline hover:text-blue-900"
							>developer.spotify.com</a
						>
					</p>
				</div>
			</div>
		</main>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted } from "vue";

// Types pour les credentials
interface CredentialForm {
	soundcloud_client_id: string;
	soundcloud_client_secret: string;
	soundcloud_user_id: string;
	spotify_client_id: string;
	spotify_client_secret: string;
}

// État du composant
const formData = ref<CredentialForm>({
	soundcloud_client_id: "",
	soundcloud_client_secret: "",
	soundcloud_user_id: "",
	spotify_client_id: "",
	spotify_client_secret: "",
});

const isLoading = ref(false);
const message = ref("");
const messageType = ref<"success" | "error">("success");

// Fonction de soumission du formulaire
async function handleSubmit() {
	try {
		isLoading.value = true;
		message.value = "";

		// Validation basique
		if (
			!formData.value.soundcloud_client_id &&
			!formData.value.spotify_client_id
		) {
			throw new Error(
				"Veuillez renseigner au moins les credentials SoundCloud ou Spotify"
			);
		}

		// Appel à l'API
		const response = await fetch(
			"http://127.0.0.1:8000/api/credentials/create-or-update",
			{
				method: "POST",
				body: JSON.stringify(formData.value),
				headers: {
					"Content-Type": "application/json",
				},
			}
		);

		if (!response.ok) {
			throw new Error(`Erreur HTTP: ${response.status}`);
		}

		const _data = await response.json();

		// Succès
		message.value = "Credentials sauvegardés avec succès !";
		messageType.value = "success";

		// Réinitialiser le formulaire après succès
		setTimeout(() => {
			message.value = "";
		}, 5000);
	} catch (error: unknown) {
		console.error("Erreur lors de la sauvegarde:", error);
		const errorMessage =
			error instanceof Error
				? error.message
				: "Erreur lors de la sauvegarde des credentials";
		message.value = errorMessage;
		messageType.value = "error";
	} finally {
		isLoading.value = false;
	}
}

// Charger les credentials existants au montage du composant
onMounted(async () => {
	try {
		const response = await fetch("http://127.0.0.1:8000/api/credentials/");
		if (response.ok) {
			const data = await response.json();
			if (data) {
				console.log(data);
				formData.value = {
					soundcloud_client_id: data.soundcloud_client_id || "",
					soundcloud_client_secret: data.soundcloud_client_secret || "",
					soundcloud_user_id: data.soundcloud_user_id?.toString() || "",
					spotify_client_id: data.spotify_client_id || "",
					spotify_client_secret: data.spotify_client_secret || "",
				};
			}
		}
	} catch (error) {
		console.error("Erreur lors de la récupération des credentials:", error);
		console.log("Aucun credential existant trouvé");
	}
});
</script>

<style scoped>
/* Styles personnalisés si nécessaire */
</style>
