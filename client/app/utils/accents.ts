// Classes écrites en entier pour que Tailwind les détecte
export const ACCENTS = {
	orange: {
		button: "bg-orange-500 hover:bg-orange-600",
		ring: "focus:ring-orange-500 focus:border-orange-500",
		link: "text-orange-600 hover:text-orange-700",
		dot: "bg-orange-500",
	},
	green: {
		button: "bg-green-600 hover:bg-green-700",
		ring: "focus:ring-green-600 focus:border-green-600",
		link: "text-green-700 hover:text-green-800",
		dot: "bg-green-600",
	},
	red: {
		button: "bg-red-600 hover:bg-red-700",
		ring: "focus:ring-red-600 focus:border-red-600",
		link: "text-red-600 hover:text-red-700",
		dot: "bg-red-600",
	},
} as const;

export type Accent = keyof typeof ACCENTS;

export const INPUT_CLASS =
	"w-full px-3 py-2 bg-white border border-gray-300 rounded-lg text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:ring-2";

export const BUTTON_CLASS =
	"inline-flex items-center justify-center gap-2 px-4 py-2 text-sm font-medium text-white rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap";

export const SECONDARY_BUTTON_CLASS =
	"inline-flex items-center justify-center gap-2 px-3 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors disabled:opacity-50 disabled:cursor-not-allowed whitespace-nowrap";
