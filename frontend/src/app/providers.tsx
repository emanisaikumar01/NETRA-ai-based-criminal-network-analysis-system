import type { ReactNode } from 'react';
import { BrowserRouter } from 'react-router-dom';

export function Providers({ children }: { children: ReactNode }) {
  return <BrowserRouter>{children}</BrowserRouter>;
}
