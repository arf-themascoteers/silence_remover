import librosa
import soundfile

waveform, sample_rate = librosa.load("speech.wav")
initial_duration = librosa.get_duration(waveform)
waveform = librosa.effects.trim(waveform, top_db=10)[0]
final_duration = librosa.get_duration(waveform)
soundfile.write("speech-trimmed.wav", waveform, sample_rate)
print(f"Initial duration: {initial_duration}. Final duration: {final_duration}")
