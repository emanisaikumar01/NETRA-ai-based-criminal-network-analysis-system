import type { ReactNode } from 'react';
import { Navigate, Route, Routes } from 'react-router-dom';
import Login from '../pages/auth/Login';
import DashboardPage from '../pages/dashboard/Dashboard';
import CasesPage from '../pages/cases/Cases';
import NetworkGraphPage from '../pages/network/NetworkGraphPage';
import LeadAnalysisPage from '../pages/leads/LeadAnalysis';
import EvidenceCoveragePage from '../pages/evidence/EvidenceCoveragePage';
import FinancialPage from '../pages/financial/FinancialIntelligencePage';
import SentinelPage from '../pages/sentinel/SentinelPage';

export const routes: Array<{ path: string; element: ReactNode }> = [
  { path: '/', element: <Navigate to="/dashboard" replace /> },
  { path: '/login', element: <Login /> },
  { path: '/dashboard', element: <DashboardPage /> },
  { path: '/cases', element: <CasesPage /> },
  { path: '/network', element: <NetworkGraphPage /> },
  { path: '/leads', element: <LeadAnalysisPage /> },
  { path: '/evidence', element: <EvidenceCoveragePage /> },
  { path: '/financial', element: <FinancialPage /> },
  { path: '/sentinel', element: <SentinelPage /> },
];

export function AppRoutes() {
  return (
    <Routes>
      {routes.map(({ path, element }) => (
        <Route key={path} path={path} element={element} />
      ))}
      <Route path="*" element={<Navigate to="/dashboard" replace />} />
    </Routes>
  );
}
