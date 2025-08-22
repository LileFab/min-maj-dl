<template>
	<div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
		<!-- Header -->
		<header class="bg-white shadow-sm border-b border-gray-200">
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
				<div class="flex justify-between items-center py-6">
					<div class="flex items-center">
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
									d="M9 19V6l12-3v13M9 19c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zm12-3c0 1.105-1.343 2-3 2s-3-.895-3-2 1.343-2 3-2 3 .895 3 2zM9 10l12-3"
								/>
							</svg>
						</div>
						<h1 class="ml-3 text-2xl font-bold text-gray-900">MinMajDL</h1>
					</div>
				</div>
			</div>
		</header>

		<!-- Main Content -->
		<main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
			<!-- Hero Section -->
			<div class="text-center mb-16">
				<h1 class="text-4xl font-bold text-gray-900 mb-6">BLABLA</h1>
				<h2 class="text-4xl font-bold text-gray-900 mb-6">
					Téléchargez votre musique en toute simplicité
				</h2>
				<p class="text-xl text-gray-600 max-w-3xl mx-auto mb-8">
					MusicDL vous permet de télécharger vos playlists SoundCloud et Spotify
					préférées avec une interface simple et intuitive.
				</p>
				<div class="flex justify-center space-x-4">
					<NuxtLink
						to="/credentials"
						class="px-8 py-3 bg-blue-600 text-white font-medium rounded-lg hover:bg-blue-700 transition-colors shadow-lg inline-block"
					>
						Renseigner mes credentials
					</NuxtLink>
				</div>
			</div>
		</main>

		<!-- Footer -->
		<footer class="bg-gray-50 border-t border-gray-200 mt-16">
			<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
				<div class="text-center text-gray-600">
					<p>&copy; 2025 MusicDL. Tous droits réservés.</p>
				</div>
			</div>
		</footer>
	</div>
</template>

<script setup lang="ts">
// Le composant est maintenant une page d'accueil statique
</script>

<style scoped>
/* Styles personnalisés si nécessaire */
</style>
