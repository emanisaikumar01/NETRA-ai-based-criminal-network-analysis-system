import { Card } from '../../components/common/Card';

export default function LeadAnalysis() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Lead analysis</h2>
      </div>

      <div className="card-grid">
        <Card title="Highest confidence">
          <ul className="clean-list">
            <li><span>Relationship ring</span><span>96%</span></li>
            <li><span>Transfer pattern</span><span>93%</span></li>
            <li><span>Location anomaly</span><span>90%</span></li>
          </ul>
        </Card>

        <Card title="Explanation summary">
          <p>Behavioral and financial signals align across repeated transactions and known entities.</p>
        </Card>
      </div>
    </div>
  );
}
