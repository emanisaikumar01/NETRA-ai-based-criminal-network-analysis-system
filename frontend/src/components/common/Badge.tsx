type BadgeProps = { label: string; tone?: 'default' | 'success' | 'warning' | 'danger' };

export function Badge({ label, tone = 'default' }: BadgeProps) {
  const colors = {
    default: '#334155',
    success: '#166534',
    warning: '#92400e',
    danger: '#991b1b',
  };

  return (
    <span
      style={{
        background: colors[tone],
        color: '#fff',
        padding: '0.25rem 0.5rem',
        borderRadius: 999,
        fontSize: 12,
      }}
    >
      {label}
    </span>
  );
}
