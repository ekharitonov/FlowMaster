// 6. Frontend Testing with Jest and React Testing Library:
// Basic test for the React component:

import { render, screen } from '@testing-library/react';
import App from './App';

test('renders welcome message', () => {
  render(<App />);
  const linkElement = screen.getByText(/Welcome to FlowMaster/i);
  expect(linkElement).toBeInTheDocument();
});
