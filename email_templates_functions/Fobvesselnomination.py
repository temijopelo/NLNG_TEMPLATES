def fob_vessel_nomination_email(cargo_id, deadline_date,fob_nomination_id,
                                send_feedback_link):
    return f""" <!doctype html>
<html>
  <body>
    <div
      style='background-color:#F5F5F5;color:#262626;font-family:"Helvetica Neue", "Arial Nova", "Nimbus Sans", Arial, sans-serif;font-size:16px;font-weight:400;letter-spacing:0.15008px;line-height:1.5;margin:0;padding:32px 0;min-height:100%;width:100%'
    >
      <table
        align="center"
        width="100%"
        style="margin:0 auto;max-width:600px;background-color:#FAFAFA"
        role="presentation"
        cellspacing="0"
        cellpadding="0"
        border="0"
      >
        <tbody>
          <tr style="width:100%">
            <td>
              <div style="padding:16px 24px 16px 24px;background-color:#e8f0f0">
                <img
                  alt="Sample product"
                  src="https://pouch.jumpshare.com/preview/j2OHpNjxoY5cdnK42kh04okk4lYhialWELU9Voc4AidUnWVTzrAkLws0wcZ-7OGc2cWq9vuQLLMgczup72392EAFtBShOikdRJ0JuyX-yJ4"
                  style="outline:none;border:none;text-decoration:none;vertical-align:top;display:inline-block;max-width:100%"
                />
              </div>
              <div style="background-color:#e8f0f0;padding:0px 56px 32px 40px">
                <div
                  style="background-color:#FFFFFF;border-radius:12px;padding:16px 24px 24px 24px"
                >
                  <div
                    style='color:#2563EB;font-size:18px;font-family:Charter, "Bitstream Charter", "Sitka Text", Cambria, serif;font-weight:bold;padding:12px 24px 0px 24px'
                  >
                    FOB Vessel Nomination
                  </div>
                  <div
                    style="font-size:14px;font-weight:bold;padding:16px 24px 16px 24px"
                  >
                    Dear Sir / Madam
                  </div>
                  <div
                    style="font-size:13px;font-weight:normal;padding:16px 24px 16px 24px"
                  >
                    Sequel to the terms stated in the sale and Purchase
                    Agreement, you are required to nominate a vessel for cargo
                    delivery for cargo {cargo_id}
                  </div>
                  <div
                    style="font-size:13px;font-weight:normal;padding:0px 24px 16px 24px"
                  >
                    Please respond with your vessel nomination by filling the
                    attached templates by {deadline_date}
                  </div>
                  <div style="padding:16px 24px 16px 24px">
                    <div
                      style="background-color:#F5F5F5;padding:16px 0px 16px 16px"
                    >
                      <table
                        align="center"
                        width="100%"
                        cellpadding="0"
                        border="0"
                        style="table-layout:fixed;border-collapse:collapse"
                      >
                        <tbody style="width:100%">
                          <tr style="width:100%">
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:50px"
                            >
                              <div style="padding:4px 8px 16px 12px">
                                <img
                                  alt=""
                                  src="https://ui-avatars.com/api/?size=128"
                                  height="32"
                                  width="32"
                                  style="outline:none;border:none;text-decoration:none;object-fit:cover;height:32px;width:32px;max-width:100%;display:inline-block;vertical-align:middle;text-align:center;border-radius:4px"
                                />
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0;width:180px"
                            >
                              <div
                                style="font-size:12px;font-weight:normal;text-align:center;padding:12px 12px 16px 12px"
                              >
                                {fob_nomination_id}
                              </div>
                            </td>
                            <td
                              style="box-sizing:content-box;vertical-align:middle;padding-left:0;padding-right:0"
                            >
                              <div
                                style="text-align:center;padding:12px 16px 16px 12px"
                              >
                                <a
                                  href="{download_link}"
                                  style="color:#000000;font-size:11px;font-weight:bold;background-color:#FFFFFF;border-radius:4px;display:inline-block;padding:8px 12px;text-decoration:none"
                                  target="_blank"
                                  ><span>Download</span></a
                                >
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
</html>"""


