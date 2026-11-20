<template>
	<section class="bg-white rounded-xl border border-gray-200">
		<div
			class="px-5 py-4 flex items-start justify-between gap-4 flex-wrap"
			:class="{ 'border-b border-gray-200': $slots.default && !flush }"
		>
			<div>
				<h3 class="font-semibold">{{ title }}</h3>
				<p v-if="description" class="mt-0.5 text-sm text-gray-500">
					{{ description }}
				</p>
			</div>
			<slot name="actions" />
		</div>
		<div v-if="$slots.default" :class="flush ? '' : 'p-5'">
			<slot />
		</div>
	</section>
</template>

<script setup lang="ts">
defineProps<{
	title: string;
	description?: string;
	/** Contenu collé aux bords (listes) */
	flush?: boolean;
}>();
</script>
