export const appConfig = {
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL ?? 'http://localhost:5000/api',
  appName: import.meta.env.VITE_APP_NAME ?? 'Case Intelligence Platform',
  authEnabled: import.meta.env.VITE_AUTH_ENABLED === 'true',
};
