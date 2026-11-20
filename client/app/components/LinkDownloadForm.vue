<template>
	<div class="space-y-3">
		<form class="flex gap-2" @submit.prevent="submit">
			<input
				v-model="link"
				type="text"
				:placeholder="placeholder"
				:class="[INPUT_CLASS, ACCENTS[accent].ring]"
			>
			<button
				type="submit"
				:disabled="isSubmitting || !link.trim()"
				:class="[BUTTON_CLASS, ACCENTS[accent].button]"
			>
				<LoadingSpinner v-if="isSubmitting" class="w-4 h-4" />
				Télécharger
			</button>
		</form>
		<DownloadStatus :status="status" />
	</div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import { ACCENTS, BUTTON_CLASS, INPUT_CLASS, type Accent } from "~/utils/accents";
import { startDownload, type DownloadResponse } from "~/utils/api";

const props = defineProps<{
	endpoint: string;
	placeholder: string;
	accent: Accent;
	/** Le lien doit correspondre, sinon `invalidMessage` est affiché */
	pattern: RegExp;
	invalidMessage: string;
}>();

const link = ref("");
const status = ref<DownloadResponse>();
const isSubmitting = ref(false);

async function submit() {
	const value = link.value.trim();
	if (!props.pattern.test(value)) {
		status.value = {
			success: false,
			message: props.invalidMessage,
			destination: "",
		};
		return;
	}

	isSubmitting.value = true;
	status.value = undefined;
	status.value = await startDownload(props.endpoint, { url: value });
	if (status.value.success) link.value = "";
	isSubmitting.value = false;
}
</script>
