export function StatCard({ label, value }: { label: string; value: string }) {
  return (
    <div className="card">
      <strong>{value}</strong>
      <div>{label}</div>
    </div>
  );
}
