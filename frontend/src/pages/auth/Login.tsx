import { Card } from '../../components/common/Card';

export default function Login() {
  return (
    <div className="page">
      <Card title="Secure sign in">
        <p>Authentication gateway for case investigators.</p>
        <button className="primary-button">Continue</button>
      </Card>
    </div>
  );
}
