export type UserRole = 'admin' | 'analyst' | 'viewer';

export interface AuthUser {
  id: string;
  name: string;
  email: string;
  role: UserRole;
}
