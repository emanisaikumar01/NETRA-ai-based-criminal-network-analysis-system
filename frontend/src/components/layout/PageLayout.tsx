type PageLayoutProps = { children: React.ReactNode };

export function PageLayout({ children }: PageLayoutProps) {
  return <div style={{ display: 'flex', minHeight: '100vh' }}>{children}</div>;
}
