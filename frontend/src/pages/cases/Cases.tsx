import { Card } from '../../components/common/Card';

export default function Cases() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Case portfolio</h2>
      </div>

      <div className="card-grid">
        <Card title="Investigation queue">
          <ul className="clean-list">
            <li><span>Asset seizure</span><span>High</span></li>
            <li><span>Vehicle linkage</span><span>Medium</span></li>
            <li><span>Beneficiary review</span><span>Low</span></li>
          </ul>
        </Card>

        <Card title="Case coverage">
          <ul className="clean-list">
            <li><span>Open reviews</span><span>34</span></li>
            <li><span>Escalated</span><span>11</span></li>
            <li><span>Closed this week</span><span>8</span></li>
          </ul>
        </Card>
      </div>
    </div>
  );
}
