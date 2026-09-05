import { Card } from '../../components/common/Card';

export default function EvidenceCoveragePage() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Evidence coverage</h2>
      </div>

      <div className="list-grid">
        <Card title="Coverage">
          <ul className="clean-list">
            <li><span>Documents</span><span>74%</span></li>
            <li><span>Financial</span><span>88%</span></li>
            <li><span>Location</span><span>68%</span></li>
          </ul>
        </Card>

        <Card title="Gaps">
          <ul className="clean-list">
            <li><span>Missing call logs</span><span>2</span></li>
            <li><span>Awaiting forensic review</span><span>5</span></li>
          </ul>
        </Card>
      </div>
    </div>
  );
}
