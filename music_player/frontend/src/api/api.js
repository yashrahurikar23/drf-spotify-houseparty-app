export const createRoom = async(payload) => {
  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  };

  const response = await fetch("/api/create-room", requestOptions);
  return await response.json();
}

export const getRoomDetails = async(roomCode) => {
  const response = await fetch(`/api/get-room?code=${roomCode}`)
  return await response.json();
}