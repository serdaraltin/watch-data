
@app.route("/api/get-blur-image/", methods=["POST"])
def get_blur_image():
    try:
        video_blur = VideoPersonBlur(MODEL_PATH)
        data = request.get_json()
        video_url = data.get("video-url")

        blurred_image = video_blur.get_blur_image(video_url)
        _, img_encoded = cv2.imencode(".jpg", blurred_image)
        bytes_io = io.BytesIO(img_encoded.tobytes())

        bytes_io.seek(0)

        # Başarılı işlemi loglama
        logging.info(f"Image successfully blurred for video: {video_url}")
        custom_logger.info(f"Image successfully blurred for video: {video_url}")

        return send_file(
            bytes_io,
            mimetype="image/jpeg",
            as_attachment=True,
            download_name="result.jpg",
        )
    except Exception as e:
        # Hata durumunda loglama
        logging.error(
            f"Error in blurring image for video: {video_url}\n{e}", exc_info=True
        )
        custom_logger.error(
            f"Error in blurring image for video: {video_url}\n{e}", exc_info=True
        )

        return jsonify({"error": str(e)}), 500
