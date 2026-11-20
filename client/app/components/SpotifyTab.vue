<template>
	<div class="space-y-6">
		<SectionCard
			title="Depuis un lien"
			description="Un titre, un album, une playlist ou un artiste Spotify (MP3 320 kbps)."
		>
			<LinkDownloadForm
				endpoint="/api/spotify/dl-playlist"
				placeholder="https://open.spotify.com/playlist/..."
				accent="green"
				:pattern="/^https:\/\/open\.spotify\.com\//"
				invalid-message="Le lien doit commencer par https://open.spotify.com/"
			/>
		</SectionCard>

		<PlaylistList
			:items="items"
			:loading="isLoading"
			:error="error"
			accent="green"
			endpoint="/api/spotify/dl-playlist"
			@refresh="fetchPlaylists"
		/>
	</div>
</template>

<script setup lang="ts">
import { computed, onMounted, ref } from "vue";
import { apiGet, type PlaylistItem } from "~/utils/api";

interface SpotifyPlaylist {
	name: string;
	dl_url: string;
	track_count: number;
	owner: string;
}

const playlists = ref<SpotifyPlaylist[]>([]);
const isLoading = ref(false);
const error = ref("");

const items = computed<PlaylistItem[]>(() =>
	playlists.value.map((p) => ({
		name: p.name,
		url: p.dl_url,
		trackCount: p.track_count,
		details: [`par ${p.owner}`],
	})),
);

async function fetchPlaylists() {
	isLoading.value = true;
	error.value = "";
	try {
		playlists.value = (await apiGet<SpotifyPlaylist[]>("/api/spotify/playlists")) ?? [];
	} catch (err: unknown) {
		error.value = err instanceof Error ? err.message : "Erreur de chargement";
		playlists.value = [];
	} finally {
		isLoading.value = false;
	}
}

onMounted(fetchPlaylists);
</script>
