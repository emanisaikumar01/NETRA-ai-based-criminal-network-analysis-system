import { Card } from '../../components/common/Card';

export default function SentinelPage() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Sentinel monitoring</h2>
      </div>

      <div className="card-grid">
        <Card title="Access anomalies">
          <ul className="clean-list">
            <li><span>After-hours access</span><span>3</span></li>
            <li><span>Unusual privilege use</span><span>1</span></li>
          </ul>
        </Card>

        <Card title="Behavior flags">
          <ul className="clean-list">
            <li><span>Credential reuse</span><span>High</span></li>
            <li><span>Pattern deviation</span><span>Medium</span></li>
          </ul>
        </Card>
      </div>
    </div>
  );
}
