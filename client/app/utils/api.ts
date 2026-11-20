import { BACKEND_URL } from "~/constants";

export interface DownloadResponse {
	success: boolean;
	message: string;
	destination: string;
}

/** Playlist affichée dans <PlaylistList> (SoundCloud ou Spotify) */
export interface PlaylistItem {
	name: string;
	url: string;
	trackCount: number;
	/** Infos secondaires affichées après le nombre de titres */
	details: string[];
}

/** Message d'erreur lisible (champ `detail` de django-ninja si présent) */
export async function readError(response: Response): Promise<string> {
	try {
		const data = await response.json();
		if (typeof data.detail === "string") return data.detail;
	} catch {
		// corps vide ou non JSON
	}
	return `Erreur HTTP ${response.status}`;
}

export async function apiGet<T>(path: string): Promise<T> {
	const response = await fetch(BACKEND_URL + path);
	if (!response.ok) throw new Error(await readError(response));
	return response.json();
}

export async function apiPost<T>(
	path: string,
	params: Record<string, string> = {},
	body?: unknown,
): Promise<T> {
	const url = new URL(BACKEND_URL + path);
	for (const [key, value] of Object.entries(params)) {
		url.searchParams.append(key, value);
	}
	const response = await fetch(url, {
		method: "POST",
		headers: body ? { "Content-Type": "application/json" } : undefined,
		body: body ? JSON.stringify(body) : undefined,
	});
	if (!response.ok) throw new Error(await readError(response));
	return response.json();
}

/** Lance un téléchargement ; ne lève jamais, renvoie l'erreur sous forme de statut */
export async function startDownload(
	path: string,
	params: Record<string, string> = {},
): Promise<DownloadResponse> {
	try {
		return await apiPost<DownloadResponse>(path, params);
	} catch (err: unknown) {
		return {
			success: false,
			message:
				err instanceof Error ? err.message : "Erreur lors du téléchargement",
			destination: "",
		};
	}
}
