<h2>Overview</h2>
<p>This project combines <strong>Columnar Transposition Cipher</strong> encryption with <strong>Least Significant Bit (LSB) Image Steganography</strong> to securely hide and extract messages from images. The encrypted message is embedded into an image, ensuring both security and confidentiality. The application is built using <strong>Streamlit</strong>, providing an easy-to-use interface.</p>

<h2>Features 🚀</h2>
<ul>
    <li><strong>Encrypt & Embed</strong>: Encrypts a message using the Columnar Transposition Cipher and hides it in an image using LSB steganography.</li>
    <li><strong>Extract & Decrypt</strong>: Extracts the hidden encrypted message from an image and decrypts it using the key.</li>
    <li><strong>Streamlit UI</strong>: A simple, interactive web-based interface for encryption, embedding, extraction, and decryption.</li>
    <li><strong>Secure & Lightweight</strong>: Provides basic encryption along with steganography for secure communication.</li>
</ul>

<h2>How It Works 🛠️</h2>
<h3>1. Encryption (Columnar Transposition Cipher)</h3>
<ul>
    <li>The text is rearranged in a grid format based on a given key.</li>
    <li>The characters are read column-wise in a new order determined by sorting the key.</li>
    <li>This scrambled text serves as the encrypted message.</li>
</ul>

<h3>2. Steganography (LSB Image Encoding)</h3>
<ul>
    <li>The encrypted text is converted into binary format.</li>
    <li>Each bit of the binary text is embedded into the least significant bit (LSB) of the image pixels.</li>
    <li>A stop marker (<code>11111111</code>) is added at the end of the message for extraction.</li>
</ul>

<h3>3. Extraction & Decryption</h3>
<ul>
    <li>The image is scanned to retrieve the hidden binary text.</li>
    <li>The extracted binary sequence is converted back into characters.</li>
    <li>The Columnar Transposition Cipher is reversed using the provided key to obtain the original message.</li>
</ul>

<h2>Installation 📦</h2>
<pre>
    git clone https://github.com/JoywinNeilLasrado/columnar-cipher-steganography.git
    cd columnar-cipher-steganography
</pre>

<h2>Usage 🔧</h2>
<pre>streamlit run app.py</pre>

<h3>Encrypt & Embed</h3>
<ol>
    <li>Upload an image (PNG/JPG/JPEG format).</li>
    <li>Enter the message to be encrypted.</li>
    <li>Provide a key for encryption.</li>
    <li>Click <strong>"Encrypt & Save"</strong> to generate an encrypted image.</li>
    <li>Download the encrypted image.</li>
</ol>

<h3>Extract & Decrypt</h3>
<ol>
    <li>Upload the previously encrypted image.</li>
    <li>Enter the decryption key.</li>
    <li>Click <strong>"Extract & Decrypt"</strong> to retrieve the original message.</li>
</ol>

<h2>Technologies Used 🛠️</h2>
<ul>
    <li><strong>Python</strong>: Core programming language</li>
    <li><strong>Streamlit</strong>: Web-based UI for interaction</li>
    <li><strong>Pillow (PIL)</strong>: Image processing</li>
    <li><strong>NumPy</strong>: Handling pixel data</li>
    <li><strong>Math</strong>: Used for calculations in encryption/decryption</li>
</ul>

<h2>Example Usage 📸</h2>
<p><strong>Encryption & Embedding:</strong></p>
<pre>
    Input Text: Hello World
    Key: KEY
    Encrypted Output: EloHl oWlrd
    Embedded into an image using LSB
</pre>
<p><strong>Extraction & Decryption:</strong></p>
<pre>
    Extracted Encrypted Text: EloHl oWlrd
    Decryption with key KEY restores: Hello World
</pre>



<h2>Limitations ⚠️</h2>
<ul>
    <li>The image must have enough pixels to store the encrypted message.</li>
    <li>The encryption is basic and not suitable for high-security applications.</li>
    <li>LSB steganography is vulnerable to image compression or modifications.</li>
</ul>

<h2>Future Improvements 🔮</h2>
<ul>
    <li>Implement stronger encryption algorithms (AES, RSA).</li>
    <li>Support for audio and video steganography.</li>
    <li>Improve UI with better visualization.</li>
</ul>

<h2>License 📜</h2>
<p>This project is open-source and available under the <strong>MIT License</strong>.</p>

<hr>
<h3>📩 Feel free to contribute or report issues!</h3>
