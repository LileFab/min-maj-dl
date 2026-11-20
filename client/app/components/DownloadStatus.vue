<template>
	<p
		v-if="status"
		class="text-sm"
		:class="status.success ? 'text-emerald-600' : 'text-red-600'"
	>
		{{ status.message }}
		<span v-if="status.success && status.destination" class="text-gray-500">
			→ {{ status.destination }}
		</span>
	</p>
</template>

<script setup lang="ts">
import type { DownloadResponse } from "~/utils/api";

defineProps<{ status?: DownloadResponse }>();
</script>
