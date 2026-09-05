import { Card } from '../../components/common/Card';

export default function NetworkGraphPage() {
  return (
    <div className="page">
      <div className="page-header">
        <h2>Network graph</h2>
      </div>

      <Card title="Relationship map">
        <p>Graph view showing entities, clusters, and relationship density.</p>
        <ul className="clean-list">
          <li><span>Core cluster</span><span>13 nodes</span></li>
          <li><span>Cross-links</span><span>42 edges</span></li>
          <li><span>High-velocity path</span><span>3 hops</span></li>
        </ul>
      </Card>
    </div>
  );
}
