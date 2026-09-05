export function EmptyState({ message = 'No data available.' }: { message?: string }) {
  return <div>{message}</div>;
}
