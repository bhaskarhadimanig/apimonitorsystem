import NextAuth from "next-auth";
import Providers from "next-auth/providers";

export default NextAuth({
  providers: [
    Providers.Google({
      clientId: process.env.GOOGLE_CLIENT_ID!,
      clientSecret: process.env.GOOGLE_CLIENT_SECRET!
    }),
    // Add GitHub, others...
  ],
  callbacks: {
    async signIn(user, account, profile) {
      // Optionally sync with your backend for user creation
      return true
    }
  }
});