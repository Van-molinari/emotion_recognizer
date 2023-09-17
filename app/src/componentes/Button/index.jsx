

export default function Button({ setAudio }) {
    return (
        <div>
            <input className="audio"
                type="file"
                accept="audio/*"
                onChange={(event) => {
                    setAudio(event.target.value)                  
                }}
            />
        </div>
    )
}
