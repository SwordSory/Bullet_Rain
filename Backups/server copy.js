import express from 'express';
import cors from 'cors';
import dotenv from 'dotenv';
import path from 'path';
import { fileURLToPath } from 'url';
import { GoogleGenAI } from '@google/genai';

dotenv.config();

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(cors());
app.use(express.json());

// ✅ Serve all static files (HTML, CSS, JS, images, etc.) from root
app.use(express.static(__dirname));

// ✅ Load index.html at root
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// ✅ Google Gemini API client
const client = new GoogleGenAI({
  apiKey: process.env.GEMINI_API_KEY,
});

// ✅ POST /get-insult
app.post('/get-insult', async (req, res) => {
  const { name, reason } = req.body;
  console.log("Received insult request for:", name, reason);

  const prompt = `Write an extremely sarcastic, and darkly funny insult targeting a person named ${name} who ${reason}. The insult should be a wild mix of Nepali (written in Roman script) and English, with a roughly equal balance between the two. Use strong, naturally flowing curse words in both languages — like randi, muji, valu, khate, motherfucker, bitch, etc. — making it sound like a brutal roast between close friends, and a serious attack. Add Nepali idioms, savage quotes, and short, original poem-like jabs to enhance the humor and creativity — but make sure the main insult content remains full and doesn’t get diluted. It should sound raw, unfiltered, emotionally charged, and street-smart, as if someone is ranting in full rage and sarcasm at a party or over voice chat. Avoid being formal or robotic — it should feel personal, wildly exaggerated, and stupidly hilarious. Text formatting not needed.

Respond only with a JSON object with a single key "insult" whose value is the insult string. Do NOT include any explanations or extra text.
Example:
{
  "insult": "Your insult here."
}
`;

  try {
    const response = await client.models.generateContent({
      model: 'gemini-2.0-flash',
      contents: prompt,
    });

    let text = response.text;

    // Remove Markdown-style ``` wrappers if present
    text = text.replace(/```json\s*([\s\S]*?)```/, '$1').trim();
    text = text.replace(/```([\s\S]*?)```/, '$1').trim();

    let insult = "Couldn’t think of an insult this time.";
    try {
      const json = JSON.parse(text);
      if (json.insult) {
        insult = json.insult;
      }
    } catch (parseError) {
      console.error("Failed to parse insult JSON:", parseError);
    }

    res.json({ insult });
  } catch (error) {
    console.error('Error generating insult:', error);
    res.status(500).json({ insult: 'Error generating insult.' });
  }
});

// ✅ POST /generate-qr
app.post('/generate-qr', async (req, res) => {
  const { text } = req.body;

  if (!text) {
    return res.status(400).json({ error: 'No text provided for QR generation.' });
  }

  try {
    const QRCode = await import('qrcode');
    const qrDataUrl = await QRCode.default.toDataURL(text);
    res.json({ qr: qrDataUrl });
  } catch (error) {
    console.error("QR generation failed:", error);
    res.status(500).json({ error: "Failed to generate QR code." });
  }
});

// ✅ Start server on LAN-accessible IP
const PORT = process.env.PORT || 3000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`✅ Server running at http://192.168.1.2:${PORT}`);
});
