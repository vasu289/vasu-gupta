// src/firebase.js
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
  apiKey: "AIzaSyDsKN6gE5FMDiRTLAqDA5cp_IPHtsCkB1E",
  authDomain: "vasu-c50a8.firebaseapp.com",
  projectId: "vasu-c50a8",
  storageBucket: "vasu-c50a8.appspot.com",
  messagingSenderId: "1024034971363",
  appId: "1:1024034971363:web:045cfe9ef623f2515d2fd6"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
