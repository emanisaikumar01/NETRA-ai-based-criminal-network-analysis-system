type ButtonProps = {
  children: React.ReactNode;
  variant?: 'primary' | 'secondary';
};

export function Button({ children, variant = 'primary' }: ButtonProps) {
  return (
    <button
      style={{
        padding: '0.6rem 1rem',
        borderRadius: 8,
        background: variant === 'primary' ? '#3b82f6' : '#1f2937',
        color: '#fff',
        border: 'none',
      }}
    >
      {children}
    </button>
  );
}
