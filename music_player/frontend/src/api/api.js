export const getRoomDetails = async(roomCode) => {
  const response = await fetch(`/api/get-room?code=${roomCode}`)
  return await response.json();
}