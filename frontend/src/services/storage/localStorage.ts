export const localStorageService = {
  get: <T>(key: string, fallback: T): T => {
    const value = window.localStorage.getItem(key);
    return value ? (JSON.parse(value) as T) : fallback;
  },
  set: (key: string, value: unknown) => {
    window.localStorage.setItem(key, JSON.stringify(value));
  },
};
