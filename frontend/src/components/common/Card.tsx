type CardProps = { title?: string; children: React.ReactNode };

export function Card({ title, children }: CardProps) {
  return (
    <section className="card">
      {title ? <h3>{title}</h3> : null}
      {children}
    </section>
  );
}
