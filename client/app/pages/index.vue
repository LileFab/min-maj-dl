<template>
	<div>
		<nav
			class="mb-6 inline-flex p-1 gap-1 bg-gray-200/70 rounded-xl text-sm font-medium"
			role="tablist"
		>
			<button
				v-for="t in TABS"
				:key="t.id"
				role="tab"
				:aria-selected="tab === t.id"
				class="flex items-center gap-2 px-4 py-2 rounded-lg transition-colors"
				:class="
					tab === t.id
						? 'bg-white text-gray-900 shadow-sm'
						: 'text-gray-600 hover:text-gray-900'
				"
				@click="selectTab(t.id)"
			>
				<span class="w-2 h-2 rounded-full" :class="ACCENTS[t.accent].dot" />
				{{ t.label }}
			</button>
		</nav>

		<!-- Chaque onglet n'est chargé qu'à sa première ouverture, puis gardé en mémoire -->
		<SoundcloudTab v-if="visited.has('soundcloud')" v-show="tab === 'soundcloud'" />
		<SpotifyTab v-if="visited.has('spotify')" v-show="tab === 'spotify'" />
		<YoutubeTab v-if="visited.has('youtube')" v-show="tab === 'youtube'" />
	</div>
</template>

<script setup lang="ts">
import { computed, reactive, watch } from "vue";
import { ACCENTS, type Accent } from "~/utils/accents";

const TABS = [
	{ id: "soundcloud", label: "SoundCloud", accent: "orange" },
	{ id: "spotify", label: "Spotify", accent: "green" },
	{ id: "youtube", label: "YouTube", accent: "red" },
] as const satisfies readonly { id: string; label: string; accent: Accent }[];

type TabId = (typeof TABS)[number]["id"];

// L'onglet actif est dans l'URL (?tab=...) : il survit au rechargement
const route = useRoute();
const router = useRouter();

const tab = computed<TabId>(() => {
	const fromUrl = route.query.tab;
	return TABS.find((t) => t.id === fromUrl)?.id ?? "soundcloud";
});

const visited = reactive(new Set<TabId>([tab.value]));
// Couvre aussi les changements d'onglet via précédent / suivant du navigateur
watch(tab, (id) => visited.add(id));

function selectTab(id: TabId) {
	router.replace({ query: { ...route.query, tab: id } });
}
</script>
