import { Card } from '../../components/common/Card';

export default function FinancialIntelligencePage() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Financial intelligence</h2>
      </div>

      <Card title="Transactional anomaly review">
        <ul className="clean-list">
          <li><span>Rapid cash movement</span><span>$48.2K</span></li>
          <li><span>Round-trip settlement</span><span>$19.7K</span></li>
          <li><span>Duplicate transfer sequence</span><span>12</span></li>
        </ul>
      </Card>
    </div>
  );
}
