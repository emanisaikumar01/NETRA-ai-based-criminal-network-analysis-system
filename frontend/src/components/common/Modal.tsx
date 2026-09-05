type ModalProps = { open: boolean; children: React.ReactNode };

export function Modal({ open, children }: ModalProps) {
  if (!open) return null;
  return (
    <div
      style={{
        position: 'fixed',
        inset: 0,
        background: 'rgba(15,23,42,0.7)',
        display: 'grid',
        placeItems: 'center',
      }}
    >
      {children}
    </div>
  );
}
