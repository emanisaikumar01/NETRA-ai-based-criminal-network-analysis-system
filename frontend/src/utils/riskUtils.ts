export function computeRiskScore(score: number) {
  return Math.min(100, Math.max(0, score));
}
