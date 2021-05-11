import os
from slack_bolt import App
from ApiCalls import getAllStatistics
from charts import getAllCharts
import matplotlib as mat


app = App(
    token=str(os.environ.get("SLACK_BOT_TOKEN")),
    signing_secret=str(os.environ.get("SLACK_SIGNING_SECRET")),
)


@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    data = getAllStatistics()
    links = getAllCharts(data)
    try:
        client.views_publish(
            user_id=event["user"],
            # the view object that appears in the app home
            view={
                "type": "home",
                "blocks": [
                        {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Covid-19 Virus Statistics",
                            }
                        },
                    {
                            "type": "divider"
                        },
                    {
                            "type": "section",
                            "fields": [
                                {
                                    "type": "plain_text",
                                    "text": "Confirmed Cases: " + str(data["confirmed"]),

                                },
                                {
                                    "type": "plain_text",
                                    "text": "Active Cases: " + str(data["active"]),

                                },
                                {
                                    "type": "plain_text",
                                    "text": "Recovered Difference: " + str(data["recovered_diff"]),

                                },
                                {
                                    "type": "plain_text",
                                    "text": "Recovered: " + str(data["recovered"]),

                                },
                                {
                                    "type": "plain_text",
                                    "text": "Deaths: " + str(data["deaths"]),

                                },
                                {
                                    "type": "plain_text",
                                    "text": "Fatality Rate: " + str(data["fatality_rate"]),

                                }
                            ]
                        },
                    {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Recovered compared to confirmed cases.",

                            }
                        },
                    {
                            "type": "divider"
                        },
                    {
                            "type": "image",
                            "image_url": links[0],
                            "alt_text": "inspiration"
                        },
                    {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Active cases compared to deaths.",

                            }
                        },
                    {
                            "type": "divider"
                        },
                    {
                            "type": "image",
                            "image_url": links[1],
                            "alt_text": "inspiration"
                        },
                    {
                            "type": "header",
                            "text": {
                                "type": "plain_text",
                                "text": "Fatality rate and survival rate.",

                            }
                        },
                    {
                            "type": "divider"
                        },
                    {
                            "type": "image",
                            "image_url": links[2],
                            "alt_text": "inspiration"
                        },
                    {
                            "type": "divider"
                        },
                    {
                            "type": "section",
                            "text": {
                                "type": "plain_text",
                                "text": "Last updated: "+str(data["last_update"]),

                            }
                        }
                ]
            }
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


@ app.error
def global_error_handler(error, body, logger):
    logger.exception(error)
    logger.info(body)


# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 2000)))
    mat.pyplot.switch_backend('Agg')
