# Unit Test

## Test Google Gemini Pro

`GOOGLE_GEMINI_API_KEY`: Through Google Gemini API Keys to get.

```shell
curl \
  -H 'Content-Type: application/json' \
  -d '{"contents":[{"parts":[{"text":"Write a story about a magic backpack"}]}]}' \
  -X POST https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=YOUR_GOOGLE_GEMINI_API_KEY
```