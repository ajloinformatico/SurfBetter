export const getMouth = (mouth) => {
    return "TODO"
}

export const setTime = (date_comment) => {
    const now = new Date()
    const year = now.getFullYear().toString()
    const mouth = now.getMonth().toString()
    const day = now.getDay().toString()
    const houre = now.getHours().toString()
    const minutes = now.getMinutes().toString()

    const date_flask = date_comment.split(" ")
    const flask_day = getDay(date_flask[0])
    const flask_mouth = date_flask[1]

    return date_flask + " " + year + " " + mouth + " " +day + " " +houre + " " + minutes
}