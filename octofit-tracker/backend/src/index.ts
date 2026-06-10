import express from 'express'
import mongoose from 'mongoose'

const app = express()
const port = process.env.PORT ? Number(process.env.PORT) : 8000
const mongoUrl = process.env.MONGODB_URI ?? 'mongodb://localhost:27017/octofit_db'

app.use(express.json())

app.get('/health', (_req, res) => {
  res.json({ status: 'ok', version: '1.0.0' })
})

mongoose
  .connect(mongoUrl)
  .then(() => {
    app.listen(port, () => {
      console.log(`OctoFit Tracker backend running on http://localhost:${port}`)
    })
  })
  .catch((error) => {
    console.error('MongoDB connection error:', error)
    process.exit(1)
  })
