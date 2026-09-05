import { Card } from '../../components/common/Card';

const stats = [
  { label: 'Open cases', value: '148' },
  { label: 'High-risk leads', value: '23' },
  { label: 'Evidence coverage', value: '82%' },
  { label: 'Active alerts', value: '7' },
];

const recentCases = [
  { name: 'Case-2048', status: 'Under review' },
  { name: 'Case-1931', status: 'Escalated' },
  { name: 'Case-1874', status: 'Awaiting data' },
];

const leadSignals = [
  { name: 'Invoice anomaly', confidence: '94%' },
  { name: 'Flagged custodian', confidence: '89%' },
  { name: 'Cross-border pattern', confidence: '82%' },
];

export default function Dashboard() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Executive dashboard</h2>
        <span className="tag">Live</span>
      </div>

      <div className="stat-grid">
        {stats.map((stat) => (
          <Card key={stat.label}>
            <div className="metric">
              <strong>{stat.value}</strong>
              <span>{stat.label}</span>
            </div>
          </Card>
        ))}
      </div>

      <div className="card-grid">
        <Card title="Recent cases">
          <ul className="clean-list">
            {recentCases.map((item) => (
              <li key={item.name}>
                <span>{item.name}</span>
                <span>{item.status}</span>
              </li>
            ))}
          </ul>
        </Card>

        <Card title="Priority leads">
          <ul className="clean-list">
            {leadSignals.map((item) => (
              <li key={item.name}>
                <span>{item.name}</span>
                <span>{item.confidence}</span>
              </li>
            ))}
          </ul>
        </Card>
      </div>
    </div>
  );
}
