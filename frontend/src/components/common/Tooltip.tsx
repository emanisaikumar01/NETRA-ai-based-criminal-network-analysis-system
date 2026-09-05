type TooltipProps = { text: string; children: React.ReactNode };

export function Tooltip({ text, children }: TooltipProps) {
  return <span title={text}>{children}</span>;
}
