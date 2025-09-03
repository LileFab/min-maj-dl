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
						<NuxtLink
							to="/credentials"
							class="px-4 py-2 text-sm font-medium text-gray-700 hover:text-gray-900 transition-colors"
						>
							Credentials
						</NuxtLink>
						<button
							class="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 transition-colors"
						>
							Profil
						</button>
					</div>
				</div>
			</div>
		</header>

		<!-- Main Content -->
		<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
			<!-- Page Title -->
			<div class="text-center mb-12">
				<h2 class="text-3xl font-bold text-gray-900 mb-4">
					Vos Playlists SoundCloud
				</h2>
				<p class="text-lg text-gray-600">
					Découvrez et gérez toutes vos playlists
				</p>
			</div>

			<!-- Stats Cards -->
			<div class="grid md:grid-cols-3 gap-6 mb-8">
				<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
					<div class="flex items-center">
						<div
							class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-6 h-6 text-blue-600"
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
						<div class="ml-4">
							<p class="text-sm font-medium text-gray-600">Total Playlists</p>
							<p class="text-2xl font-bold text-gray-900">
								{{ playlists.length }}
							</p>
						</div>
					</div>
				</div>

				<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
					<div class="flex items-center">
						<div
							class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-6 h-6 text-green-600"
								fill="none"
								stroke="currentColor"
								viewBox="0 0 24 24"
							>
								<path
									stroke-linecap="round"
									stroke-linejoin="round"
									stroke-width="2"
									d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
								/>
							</svg>
						</div>
						<div class="ml-4">
							<p class="text-sm font-medium text-gray-600">Durée Totale</p>
							<p class="text-2xl font-bold text-gray-900">
								{{ formatTotalDuration() }}
							</p>
						</div>
					</div>
				</div>

				<div class="bg-white rounded-xl shadow-sm border border-gray-200 p-6">
					<div class="flex items-center">
						<div
							class="w-12 h-12 bg-purple-100 rounded-lg flex items-center justify-center"
						>
							<svg
								class="w-6 h-6 text-purple-600"
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
						<div class="ml-4">
							<p class="text-sm font-medium text-gray-600">Total Titres</p>
							<p class="text-2xl font-bold text-gray-900">{{ totalTracks }}</p>
						</div>
					</div>
				</div>
			</div>

			<!-- Playlists Table -->
			<div
				class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden"
			>
				<!-- Table Header -->
				<div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
					<div class="flex items-center justify-between">
						<h3 class="text-lg font-semibold text-gray-900">
							Liste des Playlists
						</h3>
						<div class="flex items-center gap-3">
							<input
								v-model="searchQuerySoundcloud"
								type="text"
								placeholder="Rechercher par titre"
								class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500"
							/>
							<select
								v-model="sortKeySoundcloud"
								class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none"
							>
								<option value="title">Trier par titre</option>
								<option value="track_count">Trier par # titres</option>
							</select>
							<button
								class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-700 hover:bg-gray-100"
								@click="toggleSortOrderSoundcloud"
							>
								{{ sortOrderSoundcloud === "asc" ? "Asc" : "Desc" }}
							</button>
							<button
								:disabled="isLoading"
								class="px-4 py-2 bg-blue-600 text-white text-sm font-medium rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center"
								@click="refreshPlaylists"
							>
								<svg
									v-if="isLoading"
									class="animate-spin -ml-1 mr-2 h-4 w-4"
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
								{{ isLoading ? "Chargement..." : "Actualiser" }}
							</button>
						</div>
					</div>
				</div>

				<!-- Loading State -->
				<div
					v-if="isLoading && playlists.length === 0"
					class="p-12 text-center"
				>
					<svg
						class="animate-spin mx-auto h-12 w-12 text-blue-600 mb-4"
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
					<p class="text-gray-600">Chargement des playlists...</p>
				</div>

				<!-- Empty State -->
				<div
					v-else-if="!isLoading && playlists.length === 0"
					class="p-12 text-center"
				>
					<svg
						class="mx-auto h-12 w-12 text-gray-400 mb-4"
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
					<p class="text-gray-600 mb-2">Aucune playlist trouvée</p>
					<p class="text-sm text-gray-500">
						Vérifiez vos credentials SoundCloud
					</p>
				</div>

				<!-- Playlists Table -->
				<div v-else class="overflow-x-auto">
					<table class="min-w-full divide-y divide-gray-200">
						<thead class="bg-gray-50">
							<tr>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Playlist
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Titres
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Durée
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Dernière Modification
								</th>
								<th
									class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
								>
									Actions
								</th>
							</tr>
						</thead>
						<tbody class="bg-white divide-y divide-gray-200">
							<tr
								v-for="playlist in filteredSortedPlaylists"
								:key="playlist.permalink_url"
								class="hover:bg-gray-50 transition-colors"
							>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="flex items-center">
										<div
											class="w-10 h-10 bg-gradient-to-r from-orange-400 to-red-500 rounded-lg flex items-center justify-center"
										>
											<svg
												class="w-5 h-5 text-white"
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
										<div class="ml-4">
											<div class="text-sm font-medium text-gray-900">
												{{ playlist.title }}
											</div>
											<a
												:href="playlist.permalink_url"
												target="_blank"
												class="text-sm text-blue-600 hover:text-blue-800 transition-colors"
											>
												Voir sur SoundCloud
											</a>
										</div>
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ playlist.track_count }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ formatDuration(playlist.duration) }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap">
									<div class="text-sm text-gray-900">
										{{ formatDate(playlist.last_modified) }}
									</div>
								</td>
								<td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
									<div class="flex flex-col space-y-2">
										<!-- Bouton Télécharger -->
										<button
											:disabled="
												getDownloadStatus(playlist.permalink_url)?.message ===
												'Téléchargement en cours...'
											"
											class="text-blue-600 hover:text-blue-900 disabled:opacity-50 disabled:cursor-not-allowed transition-colors mr-3"
											@click="downloadPlaylist(playlist)"
										>
											{{
												getDownloadStatus(playlist.permalink_url)?.message ===
												"Téléchargement en cours..."
													? "Téléchargement..."
													: "Télécharger"
											}}
										</button>

										<!-- Statut du téléchargement -->
										<div
											v-if="getDownloadStatus(playlist.permalink_url)"
											class="text-xs"
										>
											<div
												:class="
													getDownloadStatus(playlist.permalink_url)?.success
														? 'text-green-600'
														: 'text-red-600'
												"
											>
												{{ getDownloadStatus(playlist.permalink_url)?.message }}
											</div>
											<div
												v-if="
													getDownloadStatus(playlist.permalink_url)?.destination
												"
												class="text-gray-500"
											>
												Destination:
												{{
													getDownloadStatus(playlist.permalink_url)?.destination
												}}
											</div>
										</div>

										<!-- Bouton Détails -->
										<button
											class="text-gray-600 hover:text-gray-900 transition-colors"
										>
											Détails
										</button>
									</div>
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</div>

			<!-- Error Message -->
			<div
				v-if="error"
				class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg"
			>
				<div class="flex items-center">
					<svg
						class="w-5 h-5 text-red-600 mr-2"
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
					<span class="text-red-800">{{ error }}</span>
				</div>
			</div>

			<!-- Spotify Section -->
			<div class="mt-16">
				<div class="text-center mb-12">
					<h2 class="text-3xl font-bold text-gray-900 mb-4">
						Vos Playlists Spotify
					</h2>
					<p class="text-lg text-gray-600">
						Découvrez et gérez vos playlists Spotify
					</p>
				</div>

				<div
					class="bg-white rounded-xl shadow-sm border border-gray-200 overflow-hidden"
				>
					<div class="px-6 py-4 border-b border-gray-200 bg-gray-50">
						<div class="flex items-center justify-between">
							<h3 class="text-lg font-semibold text-gray-900">
								Liste des Playlists
							</h3>
							<div class="flex items-center gap-3">
								<input
									v-model="searchQuerySpotify"
									type="text"
									placeholder="Rechercher par titre"
									class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none focus:ring-2 focus:ring-green-500"
								/>
								<select
									v-model="sortKeySpotify"
									class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-900 focus:outline-none"
								>
									<option value="name">Trier par titre</option>
									<option value="track_count">Trier par # titres</option>
								</select>
								<button
									class="px-3 py-2 border border-gray-300 rounded-md text-sm text-gray-700 hover:bg-gray-100"
									@click="toggleSortOrderSpotify"
								>
									{{ sortOrderSpotify === "asc" ? "Asc" : "Desc" }}
								</button>
								<button
									:disabled="isLoadingSpotify"
									class="px-4 py-2 bg-green-600 text-white text-sm font-medium rounded-lg hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors flex items-center"
									@click="refreshSpotifyPlaylists"
								>
									<svg
										v-if="isLoadingSpotify"
										class="animate-spin -ml-1 mr-2 h-4 w-4"
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
									{{ isLoadingSpotify ? "Chargement..." : "Actualiser" }}
								</button>
							</div>
						</div>
					</div>

					<div
						v-if="isLoadingSpotify && spotifyPlaylists.length === 0"
						class="p-12 text-center"
					>
						<svg
							class="animate-spin mx-auto h-12 w-12 text-green-600 mb-4"
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
						<p class="text-gray-600">Chargement des playlists Spotify...</p>
					</div>

					<div
						v-else-if="!isLoadingSpotify && spotifyPlaylists.length === 0"
						class="p-12 text-center"
					>
						<svg
							class="mx-auto h-12 w-12 text-gray-400 mb-4"
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
						<p class="text-gray-600 mb-2">Aucune playlist Spotify trouvée</p>
						<p class="text-sm text-gray-500">
							Vérifiez vos credentials Spotify
						</p>
					</div>

					<div v-else class="overflow-x-auto">
						<table class="min-w-full divide-y divide-gray-200">
							<thead class="bg-gray-50">
								<tr>
									<th
										class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Nom
									</th>
									<th
										class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Titres
									</th>
									<th
										class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Propriétaire
									</th>
									<th
										class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
									>
										Actions
									</th>
								</tr>
							</thead>
							<tbody class="bg-white divide-y divide-gray-200">
								<tr
									v-for="playlist in filteredSortedSpotifyPlaylists"
									:key="playlist.dl_url"
									class="hover:bg-gray-50 transition-colors"
								>
									<td class="px-6 py-4 whitespace-nowrap">
										<div class="text-sm font-medium text-gray-900">
											{{ playlist.name }}
										</div>
										<a
											:href="playlist.dl_url"
											target="_blank"
											class="text-sm text-green-600 hover:text-green-800 transition-colors"
											>Voir sur Spotify</a
										>
									</td>
									<td class="px-6 py-4 whitespace-nowrap">
										<div class="text-sm text-gray-900">
											{{ playlist.track_count }}
										</div>
									</td>
									<td class="px-6 py-4 whitespace-nowrap">
										<div class="text-sm text-gray-900">
											{{ playlist.owner }}
										</div>
									</td>
									<td class="px-6 py-4 whitespace-nowrap text-sm font-medium">
										<div class="flex flex-col space-y-2">
											<button
												:disabled="
													getDownloadStatus(playlist.dl_url)?.message ===
													'Téléchargement en cours...'
												"
												class="text-green-600 hover:text-green-900 disabled:opacity-50 disabled:cursor-not-allowed transition-colors mr-3"
												@click="downloadSpotifyPlaylist(playlist)"
											>
												{{
													getDownloadStatus(playlist.dl_url)?.message ===
													"Téléchargement en cours..."
														? "Téléchargement..."
														: "Télécharger"
												}}
											</button>

											<div
												v-if="getDownloadStatus(playlist.dl_url)"
												class="text-xs"
											>
												<div
													:class="
														getDownloadStatus(playlist.dl_url)?.success
															? 'text-green-600'
															: 'text-red-600'
													"
												>
													{{ getDownloadStatus(playlist.dl_url)?.message }}
												</div>
												<div
													v-if="getDownloadStatus(playlist.dl_url)?.destination"
													class="text-gray-500"
												>
													Destination:
													{{ getDownloadStatus(playlist.dl_url)?.destination }}
												</div>
											</div>
										</div>
									</td>
								</tr>
							</tbody>
						</table>
					</div>
				</div>

				<div
					v-if="spotifyError"
					class="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg"
				>
					<div class="flex items-center">
						<svg
							class="w-5 h-5 text-red-600 mr-2"
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
						<span class="text-red-800">{{ spotifyError }}</span>
					</div>
				</div>
			</div>
		</main>
	</div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";

// Types pour les playlists
interface SoundcloudPlaylist {
	title: string;
	permalink_url: string;
	duration: number;
	track_count: number;
	last_modified: string | null;
}

interface SpotifyPlaylist {
	name: string;
	dl_url: string;
	track_count: number;
	owner: string;
}

// Types pour la réponse de téléchargement
interface DownloadResponse {
	success: boolean;
	message: string;
	destination: string;
}

// État du composant
const playlists = ref<SoundcloudPlaylist[]>([]);
const spotifyPlaylists = ref<SpotifyPlaylist[]>([]);
const isLoading = ref(false);
const isLoadingSpotify = ref(false);
const error = ref("");
const spotifyError = ref("");
const downloadStatus = ref<{ [key: string]: DownloadResponse | undefined }>({});

// Recherche & tri - SoundCloud
const searchQuerySoundcloud = ref("");
const sortKeySoundcloud = ref<"title" | "track_count">("title");
const sortOrderSoundcloud = ref<"asc" | "desc">("asc");

const filteredSortedPlaylists = computed(() => {
	const query = searchQuerySoundcloud.value.trim().toLowerCase();
	const filtered = playlists.value.filter((p) =>
		p.title.toLowerCase().includes(query)
	);
	const sorted = [...filtered].sort((a, b) => {
		let comp = 0;
		if (sortKeySoundcloud.value === "title") {
			comp = a.title.localeCompare(b.title, "fr", { sensitivity: "base" });
		} else {
			comp = a.track_count - b.track_count;
		}
		return sortOrderSoundcloud.value === "asc" ? comp : -comp;
	});
	return sorted;
});

function toggleSortOrderSoundcloud() {
	sortOrderSoundcloud.value =
		sortOrderSoundcloud.value === "asc" ? "desc" : "asc";
}

// Recherche & tri - Spotify
const searchQuerySpotify = ref("");
const sortKeySpotify = ref<"name" | "track_count">("name");
const sortOrderSpotify = ref<"asc" | "desc">("asc");

const filteredSortedSpotifyPlaylists = computed(() => {
	const query = searchQuerySpotify.value.trim().toLowerCase();
	const filtered = spotifyPlaylists.value.filter((p) =>
		p.name.toLowerCase().includes(query)
	);
	const sorted = [...filtered].sort((a, b) => {
		let comp = 0;
		if (sortKeySpotify.value === "name") {
			comp = a.name.localeCompare(b.name, "fr", { sensitivity: "base" });
		} else {
			comp = a.track_count - b.track_count;
		}
		return sortOrderSpotify.value === "asc" ? comp : -comp;
	});
	return sorted;
});

function toggleSortOrderSpotify() {
	sortOrderSpotify.value = sortOrderSpotify.value === "asc" ? "desc" : "asc";
}

// Computed properties
const totalTracks = computed(() => {
	return playlists.value.reduce(
		(total, playlist) => total + playlist.track_count,
		0
	);
});

// Fonction pour obtenir le statut de téléchargement d'une playlist
function getDownloadStatus(playlistUrl: string) {
	return downloadStatus.value[playlistUrl];
}

// Fonction pour formater la durée en millisecondes
function formatDuration(ms: number): string {
	const totalSeconds = Math.floor(ms / 1000);
	const h = Math.floor(totalSeconds / 3600);
	const m = Math.floor((totalSeconds % 3600) / 60);
	const s = totalSeconds % 60;

	if (h > 0) {
		return [h, m, s].map((v) => String(v).padStart(2, "0")).join(":");
	}
	return [m, s].map((v) => String(v).padStart(2, "0")).join(":");
}

// Fonction pour formater la durée totale
function formatTotalDuration(): string {
	const totalMs = playlists.value.reduce(
		(total, playlist) => total + playlist.duration,
		0
	);
	return formatDuration(totalMs);
}

// Fonction pour formater la date
function formatDate(dateString: string | null): string {
	if (!dateString) return "N/A";

	try {
		const date = new Date(dateString);
		return date.toLocaleDateString("fr-FR", {
			year: "numeric",
			month: "short",
			day: "numeric",
			hour: "2-digit",
			minute: "2-digit",
		});
	} catch {
		return dateString as string;
	}
}

// Fonction pour récupérer les playlists SoundCloud
async function fetchPlaylists() {
	try {
		isLoading.value = true;
		error.value = "";

		const response = await fetch(
			"http://127.0.0.1:8000/api/soundcloud/playlists"
		);

		if (!response.ok) {
			throw new Error(`Erreur HTTP: ${response.status}`);
		}

		const data = await response.json();
		playlists.value = data || [];
	} catch (err: unknown) {
		console.error("Erreur lors de la récupération des playlists:", err);
		const errorMessage =
			err instanceof Error
				? err.message
				: "Erreur lors de la récupération des playlists";
		error.value = errorMessage;
		playlists.value = [];
	} finally {
		isLoading.value = false;
	}
}

// Fonction pour récupérer les playlists Spotify
async function fetchSpotifyPlaylists() {
	try {
		isLoadingSpotify.value = true;
		spotifyError.value = "";

		const response = await fetch("http://127.0.0.1:8000/api/spotify/playlists");

		if (!response.ok) {
			throw new Error(`Erreur HTTP: ${response.status}`);
		}

		const data = await response.json();
		spotifyPlaylists.value = data || [];
	} catch (err: unknown) {
		console.error("Erreur lors de la récupération des playlists Spotify:", err);
		const errorMessage =
			err instanceof Error
				? err.message
				: "Erreur lors de la récupération des playlists Spotify";
		spotifyError.value = errorMessage;
		spotifyPlaylists.value = [];
	} finally {
		isLoadingSpotify.value = false;
	}
}

// Fonction pour télécharger une playlist SoundCloud
async function downloadPlaylist(playlist: SoundcloudPlaylist) {
	try {
		// Marquer cette playlist comme en cours de téléchargement
		downloadStatus.value[playlist.permalink_url] = {
			success: false,
			message: "Téléchargement en cours...",
			destination: "",
		};

		// L'API attend le paramètre 'url' dans les query parameters
		const url = new URL("http://127.0.0.1:8000/api/soundcloud/dl-playlist");
		url.searchParams.append("url", playlist.permalink_url);

		const response = await fetch(url.toString(), {
			method: "POST",
			headers: { "Content-Type": "application/json" },
		});

		if (!response.ok) {
			let errorDetail = `Erreur HTTP: ${response.status}`;
			if (response.status === 422) {
				try {
					const errorData = await response.json();
					console.error("Détails de l'erreur 422:", errorData);
					errorDetail = `Erreur de validation: ${JSON.stringify(errorData)}`;
				} catch {
					errorDetail =
						"Erreur de validation (422) - Format de données incorrect";
				}
			}
			throw new Error(errorDetail);
		}

		const data: DownloadResponse = await response.json();
		downloadStatus.value[playlist.permalink_url] = data;

		setTimeout(() => {
			downloadStatus.value[playlist.permalink_url] = undefined;
		}, 5000);
	} catch (err: unknown) {
		console.error("Erreur lors du téléchargement:", err);
		const errorMessage =
			err instanceof Error ? err.message : "Erreur lors du téléchargement";
		downloadStatus.value[playlist.permalink_url] = {
			success: false,
			message: errorMessage,
			destination: "",
		};
		setTimeout(() => {
			downloadStatus.value[playlist.permalink_url] = undefined;
		}, 5000);
	}
}

// Fonction pour télécharger une playlist Spotify
async function downloadSpotifyPlaylist(playlist: SpotifyPlaylist) {
	try {
		// Marquer cette playlist comme en cours de téléchargement
		downloadStatus.value[playlist.dl_url] = {
			success: false,
			message: "Téléchargement en cours...",
			destination: "",
		};

		// L'API attend le paramètre 'url' dans les query parameters
		const url = new URL("http://127.0.0.1:8000/api/spotify/dl-playlist");
		url.searchParams.append("url", playlist.dl_url);

		const response = await fetch(url.toString(), {
			method: "POST",
			headers: { "Content-Type": "application/json" },
		});

		if (!response.ok) {
			let errorDetail = `Erreur HTTP: ${response.status}`;
			if (response.status === 422) {
				try {
					const errorData = await response.json();
					console.error("Détails de l'erreur 422:", errorData);
					errorDetail = `Erreur de validation: ${JSON.stringify(errorData)}`;
				} catch {
					errorDetail =
						"Erreur de validation (422) - Format de données incorrect";
				}
			}
			throw new Error(errorDetail);
		}

		const data: DownloadResponse = await response.json();
		downloadStatus.value[playlist.dl_url] = data;

		setTimeout(() => {
			downloadStatus.value[playlist.dl_url] = undefined;
		}, 5000);
	} catch (err: unknown) {
		console.error("Erreur lors du téléchargement Spotify:", err);
		const errorMessage =
			err instanceof Error ? err.message : "Erreur lors du téléchargement";
		downloadStatus.value[playlist.dl_url] = {
			success: false,
			message: errorMessage,
			destination: "",
		};
		setTimeout(() => {
			downloadStatus.value[playlist.dl_url] = undefined;
		}, 5000);
	}
}

// Fonction pour actualiser
function refreshPlaylists() {
	fetchPlaylists();
}
function refreshSpotifyPlaylists() {
	fetchSpotifyPlaylists();
}

// Charger les playlists au montage du composant
onMounted(() => {
	fetchPlaylists();
	fetchSpotifyPlaylists();
});
</script>

<style scoped>
/* Styles personnalisés si nécessaire */
</style>
