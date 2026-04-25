# CareBridge Tasks

## Authentication & Users
- [X] 1. Login page (email/password)
- [X] 2. Signup page (email/password + role selection: donor/individual/hospital)
- [X] 3. Hospital registration form (long form: name, country, city, address, establishment date, website, email, phone, workers count, Google Maps link, legal docs PDF, logo, manager photo, exterior photo, interior photo, questions, checkboxes) 
- [ ] 4. Admin approval page for pending hospitals
- [ ] 5. Role-based access control (admin/donor/individual/hospital)

## Navigation & UI
- [X] 6. Responsive navbar
- [ ] 7. Replace login button with profile icon if logged in (HTMX + backend)
- [ ] 8. Footer (all pages)
- [ ] 9. Loading states for HTMX requests
- [ ] 10. Success/error toasts (HTMX, Pico.css)
- [ ] 11. Mobile menu

## Pages
- [ ] 12. Homepage (hero, description, why, how it works, get started)
- [ ] 13. About page (mission, UNSDG3 alignment)
- [ ] 14. FAQ page (questions + legal disclaimer)
- [ ] 15. Privacy policy + terms page

## Request Forms
- [ ] 16. Individual request form (medicine name, cost, country, city, pharmacy Google Maps, pharmacy name, WhatsApp/Telegram, bill upload, urgent checkbox, swear checkbox + legal warning)
- [ ] 17. Hospital request form (anonymous patient ID, medicines, quantities, total cost, bill upload with blur instructions, urgent checkbox)

## Requests & Donations
- [ ] 18. Browse requests page (`/requests`) — list all pending requests
- [ ] 19. Request detail page — full info + pay button
- [ ] 20. Donate functionality (payment integration — Stripe/PayPal dummy or real)
- [ ] 21. Mark request as "funded" after payment
- [ ] 22. Partial payments (request stays open until fully funded)

## Dashboards
- [ ] 23. Homepage dynamic content — check user role (HTMX: logged in? which role? show corresponding dashboard or default)
- [ ] 24. Donor dashboard — past donations
- [ ] 25. Individual dashboard — their requests (pending/funded/completed)
- [ ] 26. Hospital dashboard — their patient requests + status
- [ ] 27. Admin dashboard — pending hospitals + reported requests

## Database Models
- [ ] 28. User model (email, password, name, role, phone, etc.)
- [ ] 29. Hospital model (all registration fields + verification status)
- [ ] 30. Request model (patient ID, medicines, quantities, total cost, bill photo, status, type, created by, donor, etc.)
- [ ] 31. Donation model (amount, request ID, donor ID, timestamp)

## Privacy & Legal
- [ ] 32. Bill upload instruction: "Blur your name and face. Keep medicine names + stamp visible."
- [ ] 33. Swear checkbox on all request forms (legal warning: fake = police involved)
- [ ] 34. Hospital verification photos stored securely (never public)

## Testing & Data
- [ ] 35. Seed fake data for testing (hospitals, requests, donors)
- [ ] 36. Form validation (frontend + backend)

## Deployment
- [ ] 37. Frontend deploy (Netlify)
- [ ] 38. Backend deploy (Render/Fly.io/Railway)
- [ ] 39. Environment variables setup

## Notifications
- [ ] 40. Follow button on hospital profile and request detail page
- [ ] 41. Follow button on individual request page
- [ ] 42. Notification bell icon in navbar (logged in users)
- [ ] 43. Notifications dropdown (unread count + list)
- [ ] 44. Send notification when followed hospital creates new request
- [ ] 45. Send notification when request funded (to requester)
- [ ] 46. Email notifications (optional, can be later)
- [ ] 47. Mark notification as read

## Additional
- [ ] 48. Fully responsive web design for all pages
- [ ] 49. 404 page

---

## Total: 49 tasks
