<template>
	<SectionCard
		title="Depuis un lien"
		description="Une vidéo ou une playlist YouTube. L'audio est récupéré dans la meilleure qualité disponible, sans réencodage, et rangé dans le dossier « yt-date du jour »."
	>
		<LinkDownloadForm
			endpoint="/api/youtube/dl"
			placeholder="https://www.youtube.com/watch?v=... ou /playlist?list=..."
			accent="red"
			:pattern="/^https?:\/\/((www|m|music)\.)?(youtube\.com|youtu\.be)\//"
			invalid-message="Le lien doit être un lien youtube.com ou youtu.be"
		/>
	</SectionCard>
</template>
