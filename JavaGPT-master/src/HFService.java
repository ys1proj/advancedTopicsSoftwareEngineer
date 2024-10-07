import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Headers;
import retrofit2.http.POST;

public interface HFService {
	
	final String api_key = "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";
	final String model_name = "fine-tuned-gpt2";
	
    @Headers({"Authorization: Bearer " + api_key })
    @POST(model_name)
    Call<JsonObject> queryModel(@Body JsonObject input);
}
