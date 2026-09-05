import { NavLink } from 'react-router-dom';
import { Providers } from './providers';
import { AppRoutes } from './routes';

const navItems = [
  { label: 'Dashboard', href: '/dashboard' },
  { label: 'Cases', href: '/cases' },
  { label: 'Network', href: '/network' },
  { label: 'Leads', href: '/leads' },
  { label: 'Evidence', href: '/evidence' },
  { label: 'Financial', href: '/financial' },
  { label: 'Sentinel', href: '/sentinel' },
];

export default function App() {
  return (
    <Providers>
      <div className="app-shell">
        <aside className="sidebar">
          <div className="brand">
            <div className="brand-mark">CI</div>
            <div>
              <strong>CaseIntel</strong>
              <small>Command Center</small>
            </div>
          </div>

          <nav className="sidebar-nav" aria-label="Main navigation">
            {navItems.map((item) => (
              <NavLink
                key={item.href}
                to={item.href}
                className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}
              >
                {item.label}
              </NavLink>
            ))}
          </nav>
        </aside>

        <div className="main-panel">
          <header className="topbar">
            <div>
              <p className="eyebrow">Overview</p>
              <h1>Investigation Intelligence</h1>
            </div>
            <div className="topbar-actions">
              <button className="ghost-button">Export</button>
              <button className="primary-button">New case</button>
            </div>
          </header>

          <main className="content-panel">
            <AppRoutes />
          </main>
        </div>
      </div>
    </Providers>
  );
}
