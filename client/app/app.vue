<template>
	<div class="min-h-screen bg-gray-50 text-gray-900">
		<header class="bg-white border-b border-gray-200">
			<div
				class="max-w-5xl mx-auto px-4 h-16 flex items-center justify-between"
			>
				<NuxtLink to="/" class="flex items-center gap-2">
					<span
						class="w-8 h-8 rounded-lg bg-gray-900 text-white flex items-center justify-center"
					>
						<svg
							class="w-4 h-4"
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
					</span>
					<span class="text-lg font-semibold">MinMajDL</span>
				</NuxtLink>
				<nav class="flex gap-1 text-sm font-medium">
					<NuxtLink
						to="/"
						class="px-3 py-2 rounded-lg text-gray-600 hover:text-gray-900 hover:bg-gray-100"
						exact-active-class="!text-gray-900 bg-gray-100"
					>
						Télécharger
					</NuxtLink>
					<NuxtLink
						to="/credentials"
						class="px-3 py-2 rounded-lg text-gray-600 hover:text-gray-900 hover:bg-gray-100"
						exact-active-class="!text-gray-900 bg-gray-100"
					>
						Réglages
					</NuxtLink>
				</nav>
			</div>
		</header>

		<main class="max-w-5xl mx-auto px-4 py-8">
			<NuxtPage />
		</main>
	</div>
</template>

<script setup lang="ts">
useHead({ title: "MinMajDL" });
</script>
