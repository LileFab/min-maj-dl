<template>
	<div class="space-y-6">
		<SectionCard
			title="Depuis un lien"
			description="Un titre, une playlist ou un profil SoundCloud."
		>
			<LinkDownloadForm
				endpoint="/api/soundcloud/dl-playlist"
				placeholder="https://soundcloud.com/..."
				accent="orange"
				:pattern="/^https:\/\/([a-z]+\.)?soundcloud\.com\//"
				invalid-message="Le lien doit être un lien soundcloud.com"
			/>
		</SectionCard>

		<SectionCard
			title="Mes titres likés"
			description="Dans le dossier « Likes SoundCloud ». Les titres déjà téléchargés sont ignorés."
		>
			<template #actions>
				<button
					:disabled="isSubmittingLiked"
					:class="likedButtonClass"
					@click="downloadLiked"
				>
					<LoadingSpinner v-if="isSubmittingLiked" class="w-4 h-4" />
					Télécharger mes likes
				</button>
			</template>
		</SectionCard>
		<DownloadStatus :status="likedStatus" class="-mt-4 px-1" />

		<PlaylistList
			:items="items"
			:loading="isLoading"
			:error="error"
			accent="orange"
			endpoint="/api/soundcloud/dl-playlist"
			@refresh="fetchPlaylists"
		/>
	</div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { ACCENTS, BUTTON_CLASS } from "~/utils/accents";
import {
	apiGet,
	startDownload,
	type DownloadResponse,
	type PlaylistItem,
} from "~/utils/api";

interface SoundcloudPlaylist {
	title: string;
	permalink_url: string;
	duration: number;
	track_count: number;
	last_modified: string | null;
}

const playlists = ref<SoundcloudPlaylist[]>([]);
const isLoading = ref(false);
const error = ref("");

const items = computed<PlaylistItem[]>(() =>
	playlists.value.map((p) => ({
		name: p.title,
		url: p.permalink_url,
		trackCount: p.track_count,
		details: [
			formatDuration(p.duration),
			...(p.last_modified ? [`modifiée le ${formatDate(p.last_modified)}`] : []),
		],
	})),
);

async function fetchPlaylists() {
	isLoading.value = true;
	error.value = "";
	try {
		playlists.value = (await apiGet<SoundcloudPlaylist[]>("/api/soundcloud/playlists")) ?? [];
	} catch (err: unknown) {
		error.value = err instanceof Error ? err.message : "Erreur de chargement";
		playlists.value = [];
	} finally {
		isLoading.value = false;
	}
}

// Likes
const likedStatus = ref<DownloadResponse>();
const isSubmittingLiked = ref(false);
const likedButtonClass = [BUTTON_CLASS, ACCENTS.orange.button];

async function downloadLiked() {
	isSubmittingLiked.value = true;
	likedStatus.value = await startDownload("/api/soundcloud/dl-liked");
	isSubmittingLiked.value = false;
}

// Formatage
function formatDuration(ms: number): string {
	const total = Math.floor(ms / 1000);
	const h = Math.floor(total / 3600);
	const m = Math.floor((total % 3600) / 60);
	return h > 0 ? `${h} h ${String(m).padStart(2, "0")}` : `${m} min`;
}

function formatDate(value: string): string {
	const date = new Date(value);
	return Number.isNaN(date.getTime())
		? value
		: date.toLocaleDateString("fr-FR", { day: "numeric", month: "short", year: "numeric" });
}

onMounted(fetchPlaylists);
</script>
