<template>
	<SectionCard title="Mes playlists" :description="countLabel" flush>
		<template #actions>
			<div class="flex items-center gap-2 flex-wrap">
				<input
					v-model="query"
					type="search"
					placeholder="Rechercher"
					:class="[INPUT_CLASS, ACCENTS[accent].ring, '!w-44']"
				>
				<button
					:class="SECONDARY_BUTTON_CLASS"
					title="Changer le tri"
					@click="cycleSort"
				>
					{{ sortLabel }}
				</button>
				<button
					:disabled="loading"
					:class="SECONDARY_BUTTON_CLASS"
					@click="emit('refresh')"
				>
					<LoadingSpinner v-if="loading" class="w-4 h-4" />
					Actualiser
				</button>
			</div>
		</template>

		<div
			v-if="loading && items.length === 0"
			class="p-10 flex justify-center text-gray-400"
		>
			<LoadingSpinner class="w-6 h-6" />
		</div>

		<div v-else-if="error" class="p-6 text-sm text-red-600">
			{{ error }}
			<NuxtLink to="/credentials" class="ml-1 underline">
				Vérifier les réglages
			</NuxtLink>
		</div>

		<p
			v-else-if="filtered.length === 0"
			class="p-10 text-center text-sm text-gray-500"
		>
			{{ items.length === 0 ? "Aucune playlist" : "Aucun résultat" }}
		</p>

		<ul v-else class="divide-y divide-gray-100">
			<li
				v-for="item in filtered"
				:key="item.url"
				class="px-5 py-3 flex items-center justify-between gap-4 hover:bg-gray-50"
			>
				<div class="min-w-0">
					<div class="flex items-baseline gap-2">
						<span class="font-medium truncate">{{ item.name }}</span>
						<a
							:href="item.url"
							target="_blank"
							rel="noopener"
							class="text-xs shrink-0"
							:class="ACCENTS[accent].link"
						>
							Ouvrir ↗
						</a>
					</div>
					<p class="text-sm text-gray-500">
						{{ [`${item.trackCount} titres`, ...item.details].join(" · ") }}
					</p>
					<DownloadStatus :status="statuses[item.url]" class="mt-1" />
				</div>
				<button
					:disabled="busy[item.url]"
					:class="[BUTTON_CLASS, ACCENTS[accent].button, 'shrink-0']"
					@click="download(item)"
				>
					<LoadingSpinner v-if="busy[item.url]" class="w-4 h-4" />
					Télécharger
				</button>
			</li>
		</ul>
	</SectionCard>
</template>

<script setup lang="ts">
import { computed, ref } from "vue";
import {
	ACCENTS,
	BUTTON_CLASS,
	INPUT_CLASS,
	SECONDARY_BUTTON_CLASS,
	type Accent,
} from "~/utils/accents";
import {
	startDownload,
	type DownloadResponse,
	type PlaylistItem,
} from "~/utils/api";

const props = defineProps<{
	items: PlaylistItem[];
	loading: boolean;
	error: string;
	accent: Accent;
	endpoint: string;
}>();

const emit = defineEmits<{ refresh: [] }>();

// Recherche & tri
const query = ref("");
const SORTS = [
	{ label: "Nom A→Z", compare: (a: PlaylistItem, b: PlaylistItem) => a.name.localeCompare(b.name, "fr", { sensitivity: "base" }) },
	{ label: "Nom Z→A", compare: (a: PlaylistItem, b: PlaylistItem) => b.name.localeCompare(a.name, "fr", { sensitivity: "base" }) },
	{ label: "+ de titres", compare: (a: PlaylistItem, b: PlaylistItem) => b.trackCount - a.trackCount },
	{ label: "- de titres", compare: (a: PlaylistItem, b: PlaylistItem) => a.trackCount - b.trackCount },
];
const sortIndex = ref(0);
const sortLabel = computed(() => SORTS[sortIndex.value]!.label);

function cycleSort() {
	sortIndex.value = (sortIndex.value + 1) % SORTS.length;
}

const filtered = computed(() => {
	const q = query.value.trim().toLowerCase();
	return props.items
		.filter((item) => item.name.toLowerCase().includes(q))
		.sort(SORTS[sortIndex.value]!.compare);
});

const countLabel = computed(() => {
	if (props.items.length === 0) return undefined;
	const tracks = props.items.reduce((sum, item) => sum + item.trackCount, 0);
	return `${props.items.length} playlists · ${tracks} titres`;
});

// Téléchargements (statut par playlist)
const statuses = ref<Record<string, DownloadResponse | undefined>>({});
const busy = ref<Record<string, boolean>>({});

async function download(item: PlaylistItem) {
	busy.value[item.url] = true;
	statuses.value[item.url] = undefined;
	statuses.value[item.url] = await startDownload(props.endpoint, {
		url: item.url,
	});
	busy.value[item.url] = false;
	setTimeout(() => {
		statuses.value[item.url] = undefined;
	}, 8000);
}
</script>
